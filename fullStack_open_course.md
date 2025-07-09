# [Full stack open course](https://fullstackopen.com/en/)

## [part 1 - Introduction to React](https://fullstackopen.com/en/part1)

### a Introduction to React

-  React is a JavaScript library
-  Created by Facebook (now Meta)
-  Used for building user interfaces, especially single-page applications (SPAs)

#### JSX

- The compilation is handled by Babel.
- tags must be closed: `<br />`
- root component called App at the top of the component tree
- sing fragments, i.e. by wrapping the elements to be returned by the component with an empty element:

```javascript
const App = () => {
  const name = 'Peter'
  const age = 10

  return (
    <>
      <h1>Greetings</h1>
      <Hello name='Maya' age={26 + 10} />
      <Hello name={name} age={age} />
      <Footer />
    </>
  )
}
```

-  Objects are not valid as a React child
-  In React, the individual things rendered in braces must be primitive values, such as numbers or strings:
```
const App = () => {
  const friends = [
    { name: 'Peter', age: 4 },
    { name: 'Maya', age: 10 },
  ]

  return (
    <div>
      <p>{friends[0].name} {friends[0].age}</p>
      <p>{friends[1].name} {friends[1].age}</p>
    </div>
  )
}

export default App
```

#### Exercises:

1. 

npm create vite@latest courseInformation -- --template react
npm create vite@latest courseInformation -- --template react

1 b)

Browsers do not yet support all of JavaScript's newest features. Due to this fact, a lot of code run in browsers has been transpiled from a newer version of JavaScript to an older, more compatible version.

Today, the most popular way to do transpiling is by using Babel

### b JavaScript
### c Component state, event handlers
### d A more complex state, debugging React apps



## part 2
## part 3
## part 5
## part 7a
## part 7b
## part 9c
## part 9d


The goal of going through the FullStack Open course is to be able to code a simple React app, and becoming comfortable with the useState and useEffect hooks.
Remember to take notes as you make progress. This will help you quickly review concepts during the frameworks and integration phase of Capstone.

Important articles to read after you finish the course:

- Context Api
- useReducer Hook
- useCallback Hook
- useEffect Hook
Added by
