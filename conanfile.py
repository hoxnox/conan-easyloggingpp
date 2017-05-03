from nxtools import NxConanFile
from conans import CMake, tools


class EasyloggingppConan(NxConanFile):
    name = "easyloggingpp"
    version = "9.89"
    license = ""
    url = "https://github.com/hoxnox/conan-easyloggingpp"
    license = "https://raw.githubusercontent.com/muflihun/easyloggingpp/master/LICENCE"
    settings = "os", "compiler", "build_type", "arch"
    options = {"utc_datetime":[True, False]}
    default_options = "utc_datetime=False"
    build_policy = "missing"
    description = "Logging library"

    def do_source(self):
        self.retrieve("f91f2d3d560513c8a595f5ab0b10075e8fa7ee5eb92147a0925bc9a4183e0c48",
                [
                    "vendor://easylogging/easyloggingpp/easyloggingpp_v{v}.tar.gz".format(v=self.version),
                    "https://github.com/muflihun/easyloggingpp/releases/download/{v}/easyloggingpp_v{v}.tar.gz".format(v=self.version)
                ], "easyloggingpp-{v}.tar.gz".format(v=self.version))

    def do_build(self):
        tools.untargz("easyloggingpp-{v}.tar.gz".format(v=self.version), "{staging_dir}/include".format(staging_dir = self.staging_dir))

