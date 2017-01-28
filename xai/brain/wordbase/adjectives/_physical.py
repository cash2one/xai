

#calss header
class _PHYSICAL():
	def __init__(self,): 
		self.name = "PHYSICAL"
		self.definitions = [u'relating to the body: ', u'violent: ', u'sexual: ', u'relating to things you can see or touch, or relating to the laws of nature: ', u'relating to physics: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
