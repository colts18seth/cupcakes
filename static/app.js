$("document").ready(getCupcakes);

async function getCupcakes() {
    let res = await axios.get("http://127.0.0.1:5000/api/cupcakes")
    let data = res.data.cupcakes;
    data.forEach(cupcake => {
        $("#list").append(`
        <li>
            <img src="${cupcake.image}">
            <p>Flavor: ${cupcake.flavor}</p>
            <p>Size: ${cupcake.size}</p>
            <p>Rating: ${cupcake.rating}</p>
        </li>`)
    });
    console.log(data)
}