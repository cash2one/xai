

#calss header
class _ONLY():
	def __init__(self,): 
		self.name = "ONLY"
		self.definitions = [u'used to show that something is limited to not more than, or is not anything other than, the people, things, amount, or activity stated: ', u'used to refer to something that happens almost immediately after something else: ', u'almost not: ', u'used to say that two related things are true or happened, especially when this is surprising or shocking: ', u'If you say you have only (got) to do something, you mean that it is all you need to do in order to achieve something else: ', u'used when saying that something unpleasant will happen as a result of an action or a failure to act: ', u'used to show that you feel sorry about something that cannot happen when explaining why it cannot happen: ', u'used to emphasize what you are hoping or wishing for: ', u'used to show that you think someone has done something silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
