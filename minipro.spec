%global commit 6f36b9eff8b82d5aa89f2fb07b0940383327a896
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           minipro
Version:        0
Release:        3.20140902git%{shortcommit}%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

Group:          System Environment/Base
# From the bundled debian/copyright file,
# GPLv3 text is shipped though
License:        GPLv2+
URL:            https://github.com/vdudouyt/minipro
Source0:        https://github.com/vdudouyt/minipro/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         0001-Remove-the-shebang-from-the-completion-file.patch

BuildRequires:  pkgconfig(libusb-1.0)
Requires:       udev

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
%{_bindir}/miniprohex
%{_bindir}/minipro-query-db
%{_prefix}/lib/udev/rules.d/80-minipro.rules
%{_mandir}/man1/minipro.1*


%changelog
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
