

#calss header
class _AUSTERE():
	def __init__(self,): 
		self.name = "AUSTERE"
		self.definitions = [u'very simple and without comfort or unnecessary things, especially because of severe limits on money or goods: ', u'plain and without decoration: ', u'very severe and unfriendly in manner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
