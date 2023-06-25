const counterFunction = (n) => {
    return () => {
        console.log(n)
        n++
    }
}

const something = counterFunction(1)
something()
something()
something()