%global commit e897666349cb2722edb920ed5c10ae795a2a584b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           minipro
Version:        0.1
Release:        4.20161103git%{shortcommit}%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

Group:          System Environment/Base
# From the bundled debian/copyright file,
# GPLv3 text is shipped though
License:        GPLv2+
URL:            https://github.com/vdudouyt/minipro
Source0:        https://github.com/vdudouyt/minipro/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# https://github.com/vdudouyt/minipro/pull/68
Patch0:         https://github.com/lkundrak/minipro/commit/48fb5e1a.patch#/0001-udev-split-the-uaccess-rule-into-a-separate-file.patch

BuildRequires:  pkgconfig(libusb-1.0)
Requires:       udev
Requires:       /usr/bin/srec_cat

%description
Programming utility compatible with Minipro TL866CS and Minipro TL866A
programmers. Supports more than 13000 target devices (including AVRs, PICs,
various BIOSes and EEPROMs).


%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1


%build
make %{?_smp_mflags} CFLAGS='%{optflags}'


%install
make install PREFIX=%{buildroot}%{_prefix} \
        COMPLETIONS_DIR=%{buildroot}%{_datadir}/bash-completion/completions


%post
udevadm control --reload
udevadm trigger --subsystem-match=usb --attr-match=idVendor=04d8 --attr-match=idProduct=e11c


%postun
udevadm control --reload
udevadm trigger --subsystem-match=usb --attr-match=idVendor=04d8 --attr-match=idProduct=e11c


%files
%{_datadir}/bash-completion/completions
%{_bindir}/minipro
%{_bindir}/miniprohex
%{_bindir}/minipro-query-db
%{_prefix}/lib/udev/rules.d/*-minipro.rules
%{_mandir}/man1/minipro.1*


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.1-3.20161103git484abde
- Fix the udev rule

* Thu Nov 03 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-2.20161103git484abde
- Upstreamed the patches

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-2.20161029git484abde
- Fix access for unprivileged users

* Sat Oct 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.1-1.20161029git484abde
- Update to a later snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.0.1-1
- Update to a tagged release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.20141215gitd6dee16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141215gitd6dee16
- Rebase to a later upstream snapshot

* Fri Dec 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141205git0107a7a
- Fix ATMEGA32 support
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Sat Oct 11 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141011git6a561be
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20140902git1b451ae
- Actually apply the patches...

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-5.20140902git1b451ae
- Fix insecure temporary file
- Fix PIC12 support

* Wed Oct 01 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-4.20140902git1b451ae
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Tue Sep 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-3.20140902git6f36b9e
- Patch away the shebang from completion file (Mihkel Vain, #1128356)

* Thu Sep 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-2.20140902git6f36b9e
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Sat Aug 09 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-2.20140624gite521a63
- Add a link to upstream pull request
- Don't mark bash completion nonsense as %%config (Christopher Meng, #1128356)

* Sat Aug 09 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-1.20140624gite521a63
- Initial packaging
