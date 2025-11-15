Name:           melonDS
Version:        1.0
Release:        1%{?dist}
Summary:        Nintendo DS emulator

License:        GPL-3.0
URL:            https://melonds.kuribo64.net/
Source0:        https://github.com/melonDS-emu/melonDS/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        net.kuribo64.melonDS.metainfo.xml

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  SDL2-devel
BuildRequires:  libarchive-devel
BuildRequires:  enet-devel
BuildRequires:  libzstd-devel
BuildRequires:  faad2-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  wayland-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

ExclusiveArch:  x86_64 aarch64

%description
melonDS is an open source Nintendo DS emulator. It aims to provide
accurate emulation with a focus on being fast and portable.

Features:
- Nearly complete core DS emulation
- JIT recompiler for fast emulation
- OpenGL renderer with upscaling support
- RTC emulation
- Wifi emulation
- DSi emulation (experimental)

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_QT6=ON \
    -DCMAKE_INSTALL_DO_STRIP=OFF
%cmake_build

%install
%cmake_install
install -Dm0644 %{SOURCE1} %{buildroot}%{_metainfodir}/net.kuribo64.melonDS.metainfo.xml

# Desktop file validation
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%check
# AppStream metadata validation
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml || :

%files
%license LICENSE
%doc README.md
%{_bindir}/melonDS
%{_datadir}/applications/net.kuribo64.melonDS.desktop
%{_datadir}/icons/hicolor/*/apps/net.kuribo64.melonDS.png
%{_metainfodir}/net.kuribo64.melonDS.metainfo.xml

%changelog
* Sat Nov 15 2025 Peter Jun Koh <gopeterjun@naver.com> - 1.0
- Initial package for Fedora COPR
- Built with Qt6 support
- Supports x86_64 and aarch64 architectures
