from game import App
                
app = App(412, 915, title="Piano Tiles v1.0.0")

if __name__ == "__main__":
    try:
        app.run(debug = False)
    except KeyboardInterrupt:
        pass