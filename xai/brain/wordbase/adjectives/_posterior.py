

#calss header
class _POSTERIOR():
	def __init__(self,): 
		self.name = "POSTERIOR"
		self.definitions = [u'positioned at or towards the back', u'later in time']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
