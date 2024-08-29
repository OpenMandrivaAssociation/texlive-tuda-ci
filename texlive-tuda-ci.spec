Name:		texlive-tuda-ci
Version:	71696
Release:	1
Summary:	LaTeX templates of Technische Universitat Darmstadt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tuda-ci
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tuda-ci.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tuda-ci.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The TUDa-CI-Bundle provides a possibility to use the Corporate
Design of TU Darmstadt in LaTeX. It contains documentclasses as
well as some helper packages and config files together with
some templates for user documentation, which currently are only
available in German.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tuda-ci
%doc %{_texmfdistdir}/doc/latex/tuda-ci

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
