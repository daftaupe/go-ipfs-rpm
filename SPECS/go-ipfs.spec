%define debug_package %{nil}
Name:           go-ipfs
Version:        0.4.14
Release:        1%{?dist}
Summary:        A Fast and Flexible Static Site Generator

License:        Apache 2.0
URL:            https://github.com/ipfs/%{name}
Source0:        https://github.com/ipfs/%{name}/archive/v%{version}.tar.gz

BuildRequires:  git golang systemd

AutoReq:        no 
AutoReqProv:    no

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, easy use and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

%prep
mkdir -p %{_builddir}/src/github.com/ipfs
cd %{_builddir}/src/github.com/ipfs
tar -xvzf %{_sourcedir}/v%{version}.tar.gz 
mv %{name}-%{version} %{name}
cd %{name}
make deps

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/ipfs/%{name}
make build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/usr/share/bash-completion/completions/ipfs

cp %{_builddir}/src/github.com/ipfs/%{name}/cmd/ipfs/ipfs %{buildroot}%{_bindir}
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
cp %{_builddir}/src/github.com/ipfs/%{name}/misc/completion/ipfs-completion.bash %{buildroot}/usr/share/bash-completion/completions/ipfs

%files
%{_bindir}/ipfs
%{_unitdir}ipfs.service
%{_unitdir}ipfs@.service
/usr/share/bash-completion/completions/ipfs/ipfs-completion.bash

%changelog
* Tue Apr 10 2018 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.4.14-0
- Initial rpm : version 0.4.14
