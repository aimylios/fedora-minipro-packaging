%global commit d6dee16646e07a5593d76073a0f1b7eec98f652d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           minipro
Version:        0
Release:        6.20141215git%{shortcommit}%{?dist}.1
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

Group:          System Environment/Base
# From the bundled debian/copyright file,
# GPLv3 text is shipped though
License:        GPLv2+
URL:            https://github.com/vdudouyt/minipro
Source0:        https://github.com/vdudouyt/minipro/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         0001-No-libusb_strerror-in-RHEL-7.patch

BuildRequires:  pkgconfig(libusb-1.0)
Requires:       udev
%if 0%{?rhel} == 0
Requires:       /usr/bin/srec_cat
%endif

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
make install DESTDIR=%{buildroot}


%post
udevadm control --reload
udevadm trigger --subsystem-match=usb --attr-match=idVendor=04d8 --attr-match=idProduct=e11c


%postun
udevadm control --reload
udevadm trigger --subsystem-match=usb --attr-match=idVendor=04d8 --attr-match=idProduct=e11c


%files
%{_sysconfdir}/bash_completion.d
%{_bindir}/minipro
%if 0%{?rhel}
%exclude %{_bindir}/miniprohex
%else
%{_bindir}/miniprohex
%endif
%{_bindir}/minipro-query-db
%{_prefix}/lib/udev/rules.d/80-minipro.rules
%{_mandir}/man1/minipro.1*


%changelog
* Mon Dec 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141215gitd6dee16.1
- Don't require srecord on el7

* Mon Dec 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141215gitd6dee16
- Rebase to a later upstream snapshot

* Fri Dec 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141011git6a561be.2
- Fix ATMEGA32 support

* Fri Dec 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141205git0107a7a
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Sat Oct 11 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20141011git6a561be.1
- Rebase to a later upstream snapshot
- Drop upstreamed patches

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-6.20140902git1b451ae
- Actually apply the patches...

* Tue Oct 07 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-5.20140902git1b451ae
- Fix insecure temporary file
- Fix PIC12 support

* Wed Oct 01 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-4.20140902git1b451ae.1
- Fix el6 & el7 build

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
