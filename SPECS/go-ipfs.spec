%define debug_package %{nil}
%define repo github.com/ipfs/go-ipfs
Name:           go-ipfs
Version:        0.4.14
Release:        1%{?dist}
Summary:        IPFS implementation in Go

License:        MIT
URL:            https://%{repo}
Source0:        https://%{repo}/archive/v%{version}.tar.gz

BuildRequires:  git golang systemd

AutoReq:        no 
AutoReqProv:    no

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
%setup -q -c
mkdir -p $(dirname src/%{repo})
mv %{name}-%{version} src/%{repo}
cd src/%{repo}
make deps

%build
export GOPATH="$(pwd)"
export PATH=$PATH:"$(pwd)"/bin
cd src/%{repo}
make build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/ipfs

cp src/github.com/ipfs/%{name}/cmd/ipfs/ipfs %{buildroot}%{_bindir}
cat << EOF >>  %{buildroot}%{_unitdir}ipfs.service
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
%{_unitdir}ipfs.service
%{_unitdir}ipfs@.service
%{_datadir}/bash-completion/completions/ipfs/ipfs-completion.bash
%license src/%{repo}/LICENSE

%changelog
* Tue Apr 10 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.14-0
- Initial rpm : version 0.4.14
