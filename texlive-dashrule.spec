# revision 29579
# category Package
# catalog-ctan /macros/latex/contrib/dashrule
# catalog-date 2013-03-31 13:01:15 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-dashrule
Version:	1.3
Release:	6
Summary:	Draw dashed rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashrule
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashrule.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The dashrule package makes it easy to draw a huge variety of
dashed rules (i.e., lines) in LaTeX. dashrule provides a
command, \hdashrule, which is a cross between LaTeX's \rule and
PostScript's setdash command. \hdashrule draws horizontally
dashed rules using the same syntax as \rule, but with an
additional, setdash-like parameter that specifies the pattern
of dash segments and the space between those segments. Because
dashrule's rules are constructed internally using \rule (as
opposed to, e.g., PostScript \specials) they are fully
compatible with every LaTeX back-end processor.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dashrule/dashrule.sty
%doc %{_texmfdistdir}/doc/latex/dashrule/README
%doc %{_texmfdistdir}/doc/latex/dashrule/dashrule.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dashrule/dashrule.dtx
%doc %{_texmfdistdir}/source/latex/dashrule/dashrule.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
