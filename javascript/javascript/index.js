// ExampleButton component
class ExampleButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { isCLicked: false };
    }
    render() {
        if (this.state.isCLicked) {
            return 'You clicked this';
        }
        return React.createElement(
            'button',
            { onClick: () => this.setState({ isCLicked: true }) },
            'Click me!'
        );
    }
}

// select root div
const domContainer = document.querySelector('#root');
// create the root of react dom
const root = ReactDOM.createRoot(domContainer);
// render what we see
//root.render(React.createElement(ExampleButton));

// First React Page project
root.render(React.createElement("h1", {}, "Our First React page has rendered"));
// created domContainer variable which selects HTML element with root ID (only thing react can really control)
// created root with a method within ReactDOM (defines entry point to the DOM)
// root.render allows us to render content (will overwrite whatever is in the div with root id that is an h1 and replaces it with our new elements)
// empty curly braces are for passing props and events