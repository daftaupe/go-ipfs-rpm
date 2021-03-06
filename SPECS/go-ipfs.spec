%define debug_package %{nil}
%define repo github.com/ipfs/go-ipfs
Name:           go-ipfs
Version:        0.4.16
Release:        1%{?dist}
Summary:        IPFS implementation in Go

License:        MIT
URL:            https://%{repo}
Source0:        https://%{repo}/archive/v%{version}.tar.gz

BuildRequires:  git golang systemd

AutoReq:        no 
AutoReqProv:    no

%description
IPFS implementation in Go

%prep
%setup -q -c
mkdir -p $(dirname src/%{repo})
mv %{name}-%{version} src/%{repo}

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
cd src/%{repo}
make build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/ipfs

cp src/github.com/ipfs/%{name}/cmd/ipfs/ipfs %{buildroot}%{_bindir}
cat << EOF >>  %{buildroot}%{_userunitdir}ipfs.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon

[Service]
ExecStart=/usr/bin/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
cat << EOF >> %{buildroot}%{_unitdir}ipfs@.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon

[Service]
User=%i
ExecStart=/usr/bin/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
cp src/github.com/ipfs/%{name}/misc/completion/ipfs-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/ipfs

%files
%{_bindir}/ipfs
%{_userunitdir}ipfs.service
%{_unitdir}ipfs@.service
%{_datadir}/bash-completion/completions/ipfs/ipfs-completion.bash
%license src/%{repo}/LICENSE

%changelog
* Fri Jul 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.16-1
- Update to version 0.4.16

* Sun May 13 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.15-2
- Change changelog
- Fix description

* Sat May 12 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.15-1
- Update to version 0.4.15

* Tue Apr 10 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.14-1
- Initial rpm : version 0.4.14
