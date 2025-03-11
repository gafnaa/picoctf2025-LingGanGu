Interceptor.attach(Module.findExportByName("kernel32.dll", "ReadFile"), {
    onEnter: function (args) {
        console.log("ReadFile dipanggil!");
    },
    onLeave: function (retval) {
        console.log("Hasil: " + retval.toInt32());
    }
});
