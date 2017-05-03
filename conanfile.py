from nxtools import NxConanFile
from conans import CMake, tools


class EasyloggingppConan(NxConanFile):
    name = "easyloggingpp"
    version = "9.94.2"
    license = ""
    url = "https://github.com/hoxnox/conan-easyloggingpp"
    license = "https://raw.githubusercontent.com/muflihun/easyloggingpp/master/LICENCE"
    settings = "os", "compiler", "build_type", "arch"
    options = {"utc_datetime":[True, False]}
    default_options = "utc_datetime=False"
    build_policy = "missing"
    description = "Logging library"

    def do_source(self):
        self.retrieve("15fe5c7f9bb97afd2ee7f5a449f19c9b0af3a815295ad0c93c209346af0bc830",
                [
                    "vendor://easylogging/easyloggingpp/easyloggingpp-{v}.tar.gz".format(v=self.version),
                    "https://github.com/muflihun/easyloggingpp/archive/v9.94.2.tar.gz".format(v=self.version)
                ], "easyloggingpp-{v}.tar.gz".format(v=self.version))

    def do_build(self):
        cmake = CMake(self)
        cmake.build_dir = "{staging_dir}/src".format(staging_dir=self.staging_dir)
        tools.untargz("easyloggingpp-{v}.tar.gz".format(v=self.version), cmake.build_dir)
        cmake.configure(defs={
                "CMAKE_INSTALL_PREFIX": self.staging_dir,
                "CMAKE_INSTALL_LIBDIR": "lib",
                "build_static_lib": "1",
                "lib_utc_datetime": "1" if self.options.utc_datetime else "0"
            }, source_dir="easyloggingpp-{v}".format(v=self.version))
        cmake.build(target="install")

    def do_package_info(self):
        self.cpp_info.libs = ["easyloggingpp"]

