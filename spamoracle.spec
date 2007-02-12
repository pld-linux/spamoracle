Summary:	Spam classification tool
Summary(pl.UTF-8):   Narzędzie do rozpoznawania spamu
Name:		spamoracle
Version:	1.4
Release:	1
License:	GPL v2
Vendor:		Xavier Leroy <Xavier.Leroy@inria.fr>
Group:		Applications/Mail
Source0:	http://pauillac.inria.fr/~xleroy/software/%{name}-%{version}.tar.gz
# Source0-md5:	9cd2a825202c86a3728658545b0ac060
URL:		http://pauillac.inria.fr/~xleroy/software.html
Patch0:		%{name}-latin2.patch
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SpamOracle is a tool to help detect and filter away "spam"
(unsolicited commercial e-mail). It proceeds by statistical analysis
of the words that appear in the e-mail, comparing the frequencies of
words with those found in a user-provided corpus of known spam and
known legitimate e-mail. The classification algorithm is based on
Bayes' formula, and is described in Paul Graham's paper, "A plan for
spam", <http://www.paulgraham.com/spam.html>.


%description -l pl.UTF-8
SpamOracle jest narzędziem pomagającym wykryć i odfiltrować "spam"
(niechcianą, komercyjną pocztę). Program działa w oparciu o
statystyczną analizę słów występujących w wiadomości, porównując
częstotliwość ich występowania z częstotliwością w dostarczonych przez
użytkownika zbiorach znanego spamu i dobrych maili. Algorytm
klasyfikacji jest bazowany na wzorze Bayesa, jest on opisany w pracy
Paula Grahama "A plan for spam",
<http://www.paulgraham.com/spam.html>.

%prep
%setup -q
%patch0 -p1

%build
%{__make} LANGUAGES="-DFRENCH -DSPANISH -DITALIAN -DGERMAN"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install spamoracle $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
