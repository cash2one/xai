

#calss header
class _PHYSICALLY():
	def __init__(self,): 
		self.name = "PHYSICALLY"
		self.definitions = [u"in a way that relates to the body or someone's appearance: ", u'in a way that relates to things you can see or touch or the laws of nature: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
