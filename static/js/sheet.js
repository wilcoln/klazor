class Content {
    constructor(id) {
        this.id = id
        this.editMode = true
    }
}

class VideoContent extends Content {
    constructor(id, title, video) {
        super(id)
        if(video)
            this.editMode = false
        this.title = title
        this.video = video
    }
}

class AudioContent extends Content {
    constructor(id, title, audio) {
        super(id)
        if(audio)
            this.editMode = false
        this.title = title
        this.audio = audio
    }
}

class ImageContent extends Content {
    constructor(id, title, image) {
        super(id)
        if(image)
            this.editMode = false
        this.title = title
        this.image = image
    }

}

class MarkdownContent extends Content {
    constructor(id, text) {
        super(id)
        if(text)
            this.editMode = false
        this.text = text
    }
}

class Sheet{
    constructor(title, contents){
        this.title = title
        this.contents = contents
    }
}