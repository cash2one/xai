

#calss header
class _HISTORIC():
	def __init__(self,): 
		self.name = "HISTORIC"
		self.definitions = [u'important or likely to be important in history: ', u'A historic offence is one that was committed by someone in the past but that they were not charged with at the time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
