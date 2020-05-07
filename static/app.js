$("document").ready(getCupcakes);

$("#button").on("click", addCupcake);

async function getCupcakes() {
    const res = await axios.get("http://127.0.0.1:5000/api/cupcakes")
    const data = res.data.cupcakes;
    data.forEach(cupcake => {
        $("#list").append(`
        <li>
            <img src="${cupcake.image}">
            <p>Flavor: ${cupcake.flavor}</p>
            <p>Size: ${cupcake.size}</p>
            <p>Rating: ${cupcake.rating}</p>
        </li>`)
    });
}

async function addCupcake(e) {
    e.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image = $("#image").val();

    const cupcake = {
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image
    }

    await axios.post("http://127.0.0.1:5000/api/cupcakes",
        {
            "flavor": flavor,
            "size": size,
            "rating": rating,
            "image": image
        });

    getCupcakes();
}