

#calss header
class _DISCURSIVE():
	def __init__(self,): 
		self.name = "DISCURSIVE"
		self.definitions = [u'involving discussion: ', u'talking about or dealing with subjects that are only slightly connected with the main subject for longer than necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
