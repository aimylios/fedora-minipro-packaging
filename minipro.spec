%global commit 57b293d603c5dc7217c3439a88809605d09d7293
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           minipro
Version:        0.2
Release:        1.20181017git%{shortcommit}%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

# From the bundled debian/copyright file,
# GPLv3 text is shipped though
License:        GPLv2+
URL:            https://gitlab.com/DavidGriffith/minipro
Source0:        https://gitlab.com/DavidGriffith/minipro/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# https://gitlab.com/DavidGriffith/minipro/merge_requests/126
Patch0:         0001-Revert-Renamed-Debian-udev-rules-file.patch
Patch1:         0002-Revert-Added-Centos-udev-rules-and-updated-installat.patch
Patch2:         0003-Revert-Remove-udev-and-bash-completion-installation-.patch

# https://github.com/vdudouyt/minipro/pull/68
Patch3:         https://github.com/lkundrak/minipro/commit/48fb5e1a.patch#/0001-udev-split-the-uaccess-rule-into-a-separate-file.patch

BuildRequires:  gcc
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
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
make %{?_smp_mflags} CFLAGS='%{optflags}' BUILD_DATE_TIME='20190209.190815' \
        GIT_BRANCH=master GIT_HASH=%{commit} \
        GIT_HASH_SHORT=%{shortcommit} GIT_TAG=%{version}


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} \
        COMPLETIONS_DIR=%{_datadir}/bash-completion/completions


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
%{_prefix}/lib/udev/rules.d/*-minipro.rules
%{_mandir}/man1/minipro.1*


%changelog
* Sat Feb 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1.20181017git57b293d
- Update to a newer version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20161103gite897666
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

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
