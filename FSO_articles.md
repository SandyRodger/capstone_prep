# [Context Api](https://dmitripavlutin.com/react-context-and-usecontext/)

## How to use the context
 - A. Creating the context
```
import { createContext } from 'react';

export const Context = createContext('Default Value');
```

- B. Providing the context
```
import { Context } from './context';

function Main() {
  const value = 'My Context Value';
  return (
    <Context.Provider value={value}>
      <MyComponent />
    </Context.Provider>
  );
}
```
- any component that wants to later consume the context must be wrapped in the provider component.
- When you want to update context, just update the `value` prop.
C. Consuming the context
- 2 ways:
```
import { useContext } from 'react';
import { Context } from './context';

function MyComponent() {
  const value = useContext(Context);

  return <span>{value}</span>;
}
```

2. When do you need context?
- Context solves the props drilling problem: when you have to pass down props from parents to children.
3. Use case: global user name
3.1 Context to the rescue
```
import { useContext, createContext } from 'react';

const UserContext = createContext('Unknown');

function Application() {
  const userName = "John Smith";
  return (
    <UserContext.Provider value={userName}>
      <Layout>
        Main content
      </Layout>
    </UserContext.Provider>
  );
}

function Layout({ children }) {
  return (
    <div>
      <Header />
      <main>
        {children}
      </main>
    </div>
  );
}

function Header() {
  return (
    <header>
      <UserInfo />
    </header>
  );
}

function UserInfo() {
  const userName = useContext(UserContext);
  return <span>{userName}</span>;
}
```
3.2 When context changes
4. Updating the context
5. Conclusion
# [useReducer Hook](https://dmitripavlutin.com/react-usereducer/)
# [useCallback Hook](https://dmitripavlutin.com/dont-overuse-react-usecallback/)
# [useEffect Hook](https://dmitripavlutin.com/react-useeffect-explanation/)
