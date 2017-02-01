Name     : jdk-stax-api
Version  : 1.0.1
Release  : 4
URL      : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.jar
Source0  : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.jar
Source1  : https://repo1.maven.org/maven2/stax/stax-api/1.0.1/stax-api-1.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-stax-api-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-stax-api package.
Group: Data

%description data
data components for the jdk-stax-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/stax-api.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/stax-api.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/stax-api.xml \
%{buildroot}/usr/share/maven-poms/stax-api.pom \
%{buildroot}/usr/share/java/stax-api.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/stax-api.jar
/usr/share/maven-metadata/stax-api.xml
/usr/share/maven-poms/stax-api.pom
