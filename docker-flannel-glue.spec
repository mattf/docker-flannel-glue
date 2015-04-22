Summary: Integration glue to link Docker and Flannel
Name: docker-flannel-glue
Version: 0.1
Release: 1
License: GPL
URL: none
Source0: flannel-docker-bridge
Source1: flannel-docker-bridge.service
Source2: flannel.conf
Source3: flannel-docker-bridge.conf
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: systemd-units

%description
Integration glue to link Docker and Flannel.

%prep
rm -rf %name-%version
mkdir %name-%version
cp -p %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %name-%version

%build

%install
cd %name-%version

mkdir -p %buildroot/%_libexecdir
mkdir -p %buildroot/%_unitdir
mkdir -p %buildroot/%_unitdir/docker.service.d
mkdir -p %buildroot/%_unitdir/flanneld.service.d

install -m 0755 flannel-docker-bridge         %buildroot/%_libexecdir
install -m 0644 flannel-docker-bridge.service %buildroot/%_unitdir
install -m 0644 flannel.conf                  %buildroot/%_unitdir/docker.service.d
install -m 0644 flannel-docker-bridge.conf    %buildroot/%_unitdir/flanneld.service.d

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%_libexecdir/flannel-docker-bridge
%_unitdir/flannel-docker-bridge.service
%_unitdir/docker.service.d/flannel.conf
%_unitdir/flanneld.service.d/flannel-docker-bridge.conf


%changelog
* Tue Apr 21 2015 Matthew Farrellee <matt@redhat> - 0.1-1
- Code from Lars Kellogg-Stedman

