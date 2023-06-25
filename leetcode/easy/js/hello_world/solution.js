// 2667. Create Hello World Function
// Write a function createHelloWorld. It should return a new function that always returns "Hello World".

const createHelloWorld = () => {
    return () => {
        return "Hello World"
    }
}

const something = createHelloWorld()
something()