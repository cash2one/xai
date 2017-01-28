

#calss header
class _GREY():
	def __init__(self,): 
		self.name = "GREY"
		self.definitions = [u'of the colour that is a mixture of black and white, the colour of rain clouds: ', u'having hair that has become grey or white, usually because of age: ', u'used to describe the weather when there are a lot of clouds and little light: ', u'boring and sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
