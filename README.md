# go-ipfs rpm

## RPM Build

#### Install rpmbuild requirements

```
yum install -y spectool git mock
```

### Setup build environment

```
cd ~
git clone https://gitlab.com/daftaupe/go-ipfs-rpm.git
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
ln -s ~/go-ipfs-rpms/SPECS/go-ipfs.spec ~/rpmbuild/SPECS/go-ipfs.spec
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
cd ~/rpmbuild/SOURCES/
spectool -g ../SPECS/go-ipfs.spec
cd ~/rpmbuild/SPECS/
```
### Build the SRPM
```
rpmbuild -bs ~/rpmbuild/SPECS/go-ipfs.spec
# Get the SRPM in ~/rpmbuild/SRPMS
```

### Build the RPM from the SRPM
You build it as indicated before (in that case be careful about the name of the SRPM you will get).
```
#RPM file will be found in ~/rpmbuild/RPMS
# Centos7-64bits
mock --cleanup-after --resultdir ~/rpmbuild/RPMS -r epel-7-x86_64 ~/rpmbuild/SRPMS/go-ipfs-0.4.14-1.el7.src.rpm
# Fedora-27-64bits
mock --cleanup-after --resultdir ~/rpmbuild/SRPMS -r fedora-27-x86_64 ~/rpmbuild/SRPMS/go-ipfs-0.4.14-1.fc27.src.rpm
```

### Usage

See the official [documentation](https://ipfs.io/docs/getting-started)
