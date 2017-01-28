

#calss header
class _MULTIMEDIA():
	def __init__(self,): 
		self.name = "MULTIMEDIA"
		self.definitions = [u'using a combination of moving and still pictures, sound, music, and words, especially in computers or entertainment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
