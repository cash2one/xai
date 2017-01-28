

#calss header
class _SWEET():
	def __init__(self,): 
		self.name = "SWEET"
		self.definitions = [u'(especially of food or drink) having a taste similar to that of sugar; not bitter or salty: ', u'If an emotion or event is sweet, it is very pleasant and satisfying: ', u'If a sound is sweet, it is pleasant and easy to like: ', u'(especially of something or someone small) pleasant and attractive: ', u'kind and pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
