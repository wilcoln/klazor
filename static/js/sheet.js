class Content {
    constructor(id) {
        this.id = id
        this.editMode = true
    }
}

class VideoContent extends Content {
    constructor(id, title, video, displayWidth) {
        super(id)
        if (video) {
            this.editMode = false
            this.filename = video.substring(14)
        }
        this.title = title
        this.video = video
        this.displayWidth = displayWidth
    }
}

class AudioContent extends Content {
    constructor(id, title, audio) {
        super(id)
        if (audio){
            this.editMode = false
            this.filename = audio.substring(14)
        }
        this.title = title
        this.audio = audio
    }
}

class ImageContent extends Content {
    constructor(id, title, image, displayWidth) {
        super(id)
        if (image){
            this.editMode = false
            this.filename = image.substring(14)
        }
        this.title = title
        this.image = image
        this.displayWidth = displayWidth
    }

}

class MarkdownContent extends Content {
    constructor(id, text) {
        super(id)
        if (text)
            this.editMode = false
        this.text = text
    }
}