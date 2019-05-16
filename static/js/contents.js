class Content {
    }
    class VideoContent extends  Content{
        constructor(title, video){
            super()
            this.title = title
            this.video = video
        }
    }
    class AudioContent extends  Content{
        constructor(title, audio){
            super()
            this.title = title
            this.audio = audio
        }
    }
    class ImageContent extends Content{
            constructor(title, image){
                super()
                this.title = title
                this.image = image
            }

    }
    class MarkdownContent extends Content{
            constructor(text){
                super()
                this.text = text
            }
    }