class Cell {
    constructor(id) {
        this.id = id
        this.editMode = true
        this.selected = true
    }
}

class VideoCell extends Cell {
    constructor(id, title, video, scale) {
        super(id)
        if (video) {
            this.editMode = false
            this.filename = video.substring(14)
        }
        this.title = title
        this.video = video
        this.scale = scale
    }
}

function getVideoId(url){
    url = url.replace('&t', '')
    let urlparts = url.split('/')
    urlparts = urlparts[urlparts.length - 1].split('=')
    let videoId = urlparts.length > 1 ? urlparts[1]: urlparts[0]
    return videoId
}
class YoutubeCell extends Cell {
    constructor(id, title, youtube, scale) {
        super(id)
        this.title = title
        if(youtube)
            this.editMode = false
        this.youtube = youtube
        this.scale = scale
    }
    embedUrl(){
        let videoId = getVideoId(this.youtube)
        this.youtube =  'https://www.youtube.com/embed/' + videoId
        return this.youtube
    }
}
class AudioCell extends Cell {
    constructor(id, title, audio) {
        super(id)
        if (audio){
            this.editMode = false
            this.filename = getFilenameFromUrl(audio)
        }
        this.title = title
        this.audio = audio
    }
}

class ImageCell extends Cell {
    constructor(id, title, image, scale) {
        super(id)
        if (image){
            this.editMode = false
            this.filename = getFilenameFromUrl(image)
        }
        this.title = title
        this.image = image
        this.scale = scale
    }
}

class MarkdownCell extends Cell {
    constructor(id, text) {
        super(id)
        if (text)
            this.editMode = false
        this.text = text
    }
}

class FileCell extends Cell {
    constructor(id, title, file) {
        super(id)
        if (file){
            this.editMode = false
            this.filename = getFilenameFromUrl(file)
        }
        this.title = title
        this.file = file
    }
}

class QuestionCell extends Cell{
    constructor(id, question){
        super(id)
        this.question = question
    }
}

class MultipleChoiceQuestionCell extends QuestionCell{
    constructor(id, question, propositions){
        super(id, question)
        //TODO : continue
    }
}

function getFilenameFromUrl(url){
    let urlparts = url.split('/')
    return urlparts[urlparts.length - 1]
}