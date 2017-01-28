

#calss header
class _STACCATO():
	def __init__(self,): 
		self.name = "STACCATO"
		self.definitions = [u'used to describe musical notes that are short and separate when played, or this way of playing music: ', u'used to describe a noise or way of speaking that consists of a series of short and separate sounds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
