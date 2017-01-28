

#calss header
class _CONSERVATIVE():
	def __init__(self,): 
		self.name = "CONSERVATIVE"
		self.definitions = [u'not usually liking or trusting change, especially sudden change: ', u'If you are conservative in your appearance, you usually do not like fashionable or modern clothes or hairstyles: ', u'A conservative guess or calculation is likely to be less than the real amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
