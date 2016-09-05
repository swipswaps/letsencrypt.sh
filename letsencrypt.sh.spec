Name:		letsencrypt.sh
Version: 1.0.2
Release: 1%{?dist}
Summary:	letsencrypt/acme client implemented as a shell-script

License:	MIT	
URL:		https://github.com/NethServer/letsencrypt.sh
Source0:	https://github.com/NethServer/letsencrypt.sh/archive/master.tar.gz

BuildArch:	noarch
Requires:	openssl

%description
letsencrypt/acme client implemented as a shell-script

%prep
%setup -n letsencrypt.sh-master


%build
rm -rf %{buildroot}

%install
install -D -m 0555 letsencrypt.sh %{buildroot}/%{_sbindir}/letsencrypt.sh
install -D -m 0644 docs/examples/config %{buildroot}/%{_sysconfdir}/%{name}/config.sh
install -D -m 0644 docs/examples/domains.txt %{buildroot}/%{_sysconfdir}/%{name}/domains.txt
install -D -m 0644 docs/examples/hook.sh %{buildroot}/%{_sysconfdir}/%{name}/hook.sh.example


%files
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.sh
%config %{_sysconfdir}/%{name}/domains.txt
%ghost %{_sysconfdir}/%{name}/hook.sh.example
%doc README.md LICENSE
%{_sbindir}/letsencrypt.sh



%changelog
* Mon Sep 05 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Mark config file as noreplace

* Fri Sep 02 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Let's Encrypt: certificates not renewed - Bug #3420

* Mon Jun 06 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Updated to latest upstream release [NethServer - #3399]

* Tue Feb 16 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.0.1-1
- First build for CentOS

