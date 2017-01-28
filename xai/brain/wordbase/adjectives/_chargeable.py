

#calss header
class _CHARGEABLE():
	def __init__(self,): 
		self.name = "CHARGEABLE"
		self.definitions = [u'If something is chargeable, you can be asked to pay for it: ', u'If something is chargeable, you have to pay tax on it: ', u'If something is chargeable, it is an offence that you can be charged with (= formally accused of) under the law: ', u'able to be recharged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
