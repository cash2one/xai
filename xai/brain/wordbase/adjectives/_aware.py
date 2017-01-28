

#calss header
class _AWARE():
	def __init__(self,): 
		self.name = "AWARE"
		self.definitions = [u'knowing that something exists, or having knowledge or experience of a particular thing: ', u'having special interest in or experience of something and so knowing what is happening in that subject at the present time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
