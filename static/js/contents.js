class Content {
    constructor(id) {
        this.id = id
    }
}

class VideoContent extends Content {
    constructor(id, title, video) {
        super(id)
        this.title = title
        this.video = video
    }
}

class AudioContent extends Content {
    constructor(id, title, audio) {
        super(id)
        this.title = title
        this.audio = audio
    }
}

class ImageContent extends Content {
    constructor(id, title, image) {
        super(id)
        this.title = title
        this.image = image
    }

}

class MarkdownContent extends Content {
    constructor(id, text) {
        super(id)
        this.text = text
    }
}