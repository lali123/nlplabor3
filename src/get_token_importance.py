import torch

def get_token_importance(model, input_ids, attention_mask):
    embeddings = model.get_input_embeddings()(input_ids)
    embeddings.retain_grad()
    
    output = model(inputs_embeds=embeddings, attention_mask=attention_mask)
    loss = output.logits.max()
    loss.backward()
    
    importance = embeddings.grad.abs().sum(dim=-1)
    return importance / importance.max()
