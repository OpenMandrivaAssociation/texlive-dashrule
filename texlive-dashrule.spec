%global tl_name dashrule
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Draw dashed rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dashrule
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The dashrule package makes it easy to draw a huge variety of dashed
rules (i.e., lines) in LaTeX. dashrule provides a command, \hdashrule,
which is a cross between LaTeX's \rule and PostScript's setdash command.
\hdashrule draws horizontally dashed rules using the same syntax as
\rule, but with an additional, setdash-like parameter that specifies the
pattern of dash segments and the space between those segments. Because
dashrule's rules are constructed internally using \rule (as opposed to,
e.g., PostScript \specials) they are fully compatible with every LaTeX
back-end processor.

