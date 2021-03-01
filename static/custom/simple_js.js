$(function () {
    new Vue({
        el: "#simple",
        data: {
            names: "",
            address: "",
            phone: ""
        },
        methods: {
            save() {
                let form_data = new FormData();

                    form_data.append("name", this.names);
                    form_data.append("address", this.address);
                    form_data.append("address", this.phone);

                axios.post('/', form_data).then(response => {
                        console.log(response);
                        if (response.data.errors.length)
                            console.log(response.data.errors);
                        else
                            window.location.href = '/';
                    }
                ).catch(
                    error => {
                        console.log("error");
                        console.log(error);
                    }
                );
            },
        }
    });
});