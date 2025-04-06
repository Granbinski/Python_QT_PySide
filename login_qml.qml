import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow{

  visible: true
  font.pixelSize:24
  width: 600
  height: 500
  Material.theme: 'Dark'

Row{

  id: row
  spacing: 20
  anchors {
    horizontalCenter: parent.horizontalCenter
    top: parent.top
    topMargin: 80
  }

  TextField{
    id: pokemon_id
    placeholderText: 'Pokemon id!'
    width: 200
  }
  Button{
    text: 'Get!'
    width: 200
    onClicked:{
      var fetch_return = ponte.fetch_image(pokemon_id.text)
		  pokemon_id.text = ''
		  img.source = ''
		  label.text = fetch_return[1]
      img.source = fetch_return[0]
	    }
    }
  }
    Label{
    id:label
    text:'Pokemon!'
    anchors{
      horizontalCenter: parent.horizontalCenter
      top: row.top
      topMargin: 60
  }

  }

  Image{
    id: img
    width: 300
    height: 300
    cache: false
    anchors {
    horizontalCenter: parent.horizontalCenter
    top: row.top
    topMargin: 80
    }
  }
}