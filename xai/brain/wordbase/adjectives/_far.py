

#calss header
class _FAR():
	def __init__(self,): 
		self.name = "FAR"
		self.definitions = [u'used to refer to something that is not near, or the part of something that is most distant from the centre or from you: ', u'used to refer to political groups whose opinions are very extreme: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
