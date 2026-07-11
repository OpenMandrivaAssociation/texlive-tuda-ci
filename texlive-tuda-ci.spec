%global tl_name tuda-ci
%global tl_revision 79326

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.06
Release:	%{tl_revision}.1
Summary:	LaTeX templates of Technische Universitat Darmstadt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tuda-ci
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tuda-ci.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tuda-ci.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tuda-ci.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The TUDa-CI-Bundle provides a possibility to use the Corporate Design of
TU Darmstadt in LaTeX. It contains documentclasses as well as some
helper packages and config files together with some templates for user
documentation, which currently are only available in German.

