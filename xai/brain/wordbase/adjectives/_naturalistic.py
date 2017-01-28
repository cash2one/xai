

#calss header
class _NATURALISTIC():
	def __init__(self,): 
		self.name = "NATURALISTIC"
		self.definitions = [u'Naturalistic art, literature, acting, etc. shows things as they really are.', u'similar to what exists in nature: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
