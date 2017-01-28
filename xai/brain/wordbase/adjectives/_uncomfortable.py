

#calss header
class _UNCOMFORTABLE():
	def __init__(self,): 
		self.name = "UNCOMFORTABLE"
		self.definitions = [u'not feeling comfortable and pleasant, or not making you feel comfortable and pleasant: ', u'slightly embarrassed, or making you feel slightly embarrassed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
