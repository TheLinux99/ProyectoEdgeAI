DESCRIPTION = "Simple Python setuptools hello world application"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://setup.sh \
           file://start.sh \
           "

S = "${WORKDIR}"

do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 setup.sh ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 start.sh ${D}${bindir}
}
