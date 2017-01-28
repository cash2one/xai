

#calss header
class _SYNDICATED():
	def __init__(self,): 
		self.name = "SYNDICATED"
		self.definitions = [u'(of articles and photographs) sold to several different newspapers and magazines for publishing', u'(of television or radio programmes) sold to several different broadcasting organizations']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
