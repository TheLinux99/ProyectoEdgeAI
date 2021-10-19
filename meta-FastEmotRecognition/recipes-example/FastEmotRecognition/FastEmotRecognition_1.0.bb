DESCRIPTION = "Simple Python setuptools hello world application"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://main_lite.py \
           file://haarcascade_frontalface_default.xml \
           file://_config.yml \
           file://_layouts/default.html \
           file://models/model.tflite \
           file://models/model_optimized.tflite \
           "

S = "${WORKDIR}"

do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 main_lite.py ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 haarcascade_frontalface_default.xml ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 _config.yml ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 _layouts/default.html ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 models/model.tflite ${D}${bindir}
    
    install -d ${D}${bindir}
    install -m 0755 models/model_optimized.tflite ${D}${bindir}
}
